#!/usr/bin/env python3
"""Crawl a public sitemap into Markdown pages and a searchable CSV index."""
from __future__ import annotations
import argparse,csv,re,time,urllib.parse,urllib.request,urllib.robotparser,xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor,as_completed
from datetime import datetime,timezone
from pathlib import Path
from bs4 import BeautifulSoup
from markdownify import markdownify
from scrapling.fetchers import Fetcher

def fetch_text(url):
    req=urllib.request.Request(url,headers={"User-Agent":"SenlinKnowledgeCrawler/1.0"})
    with urllib.request.urlopen(req,timeout=30) as r:return r.read().decode("utf-8",errors="replace")

def sitemap_urls(url):
    root=ET.fromstring(fetch_text(url))
    return [n.text.strip() for n in root.iter() if n.tag.endswith("loc") and n.text]

def safe_rel_path(url):
    parts=[urllib.parse.unquote(p) for p in urllib.parse.urlparse(url).path.strip("/").split("/") if p]
    lang="en" if parts and parts[0]=="en" else "zh"
    if lang=="en":parts=parts[1:]
    if not parts:parts=["index"]
    parts=[re.sub(r"[^A-Za-z0-9._-]+","-",p).strip("-") or "page" for p in parts]
    return Path(lang,*parts).with_suffix(".md")

def clean_markdown(html):
    soup=BeautifulSoup(html,"html.parser")
    title_node=soup.find("h1") or soup.find("title")
    title=title_node.get_text(" ",strip=True) if title_node else "Untitled"
    desc=soup.find("meta",attrs={"name":"description"})
    description=desc.get("content","").strip() if desc else ""
    main=soup.find("main") or soup.find("article") or soup.find(attrs={"role":"main"}) or soup.body or soup
    for node in main.select("script,style,noscript,svg,nav,footer,header"):node.decompose()
    text=markdownify(str(main),heading_style="ATX",bullets="-")
    return title,description,re.sub(r"\n{3,}","\n\n",text).strip()

def quote(v):return '"'+v.replace("\\","\\\\").replace('"','\\"').replace("\n"," ")+'"'

def crawl_one(url,output,delay):
    if delay:time.sleep(delay)
    response=Fetcher.get(url,stealthy_headers=True,timeout=30)
    title,description,body=clean_markdown(response.html_content)
    if len(body)<80:raise ValueError(f"extracted content too short: {len(body)}")
    rel=safe_rel_path(url); target=output/"pages"/rel; target.parent.mkdir(parents=True,exist_ok=True)
    lang="en" if rel.parts[0]=="en" else "zh"
    parts=urllib.parse.urlparse(url).path.strip("/").split("/")
    category=parts[1] if lang=="en" and len(parts)>1 else (parts[0] if parts and parts[0] else "home")
    fetched=datetime.now(timezone.utc).isoformat(timespec="seconds")
    fm="\n".join(["---","type: web_source",f"source_url: {quote(url)}",f"title: {quote(title)}",f"language: {lang}",f"category: {quote(category)}",f"fetched_at: {fetched}","---",""])
    target.write_text(fm+body+"\n",encoding="utf-8")
    summary=description or re.sub(r"[#*`>|\[\]()]","",body).replace("\n"," ")[:240]
    return {"title":title,"url":url,"language":lang,"category":category,"file":target.relative_to(output).as_posix(),"summary":summary,"status":"ok"}

def write_csv(path,rows,fields):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8-sig",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)

def main():
    p=argparse.ArgumentParser();p.add_argument("site");p.add_argument("output",type=Path);p.add_argument("--sitemap");p.add_argument("--max-pages",type=int,default=0);p.add_argument("--workers",type=int,default=4);p.add_argument("--delay",type=float,default=.15);a=p.parse_args()
    site=a.site.rstrip("/"); sitemap=a.sitemap or site+"/sitemap.xml"; host=urllib.parse.urlparse(site).netloc
    robot=urllib.robotparser.RobotFileParser(urllib.parse.urljoin(site+"/","robots.txt"));robot.read()
    urls=[u for u in sitemap_urls(sitemap) if urllib.parse.urlparse(u).netloc==host and robot.can_fetch("SenlinKnowledgeCrawler/1.0",u)]
    urls=list(dict.fromkeys(urls));urls=urls[:a.max_pages] if a.max_pages else urls;a.output.mkdir(parents=True,exist_ok=True)
    rows=[];fails=[];print(f"Crawling {len(urls)} pages from {site}")
    with ThreadPoolExecutor(max_workers=max(1,a.workers)) as pool:
        futures={pool.submit(crawl_one,u,a.output,a.delay):u for u in urls}
        for i,f in enumerate(as_completed(futures),1):
            try:rows.append(f.result())
            except Exception as e:fails.append({"url":futures[f],"error":str(e)})
            if i%25==0 or i==len(urls):print(f"  {i}/{len(urls)} complete; failures={len(fails)}")
    rows.sort(key=lambda r:(r["language"],r["category"],r["title"]))
    write_csv(a.output/"index.csv",rows,["title","url","language","category","file","summary","status"]);write_csv(a.output/"failures.csv",fails,["url","error"])
    readme=f"# Website Knowledge Archive\n\n- Source: {site}\n- Sitemap: {sitemap}\n- Crawled at: {datetime.now().astimezone().isoformat(timespec='seconds')}\n- Successful pages: {len(rows)}\n- Failed pages: {len(fails)}\n\nOpen `index.csv` for filtering, or search `pages/` with Obsidian or ripgrep.\n"
    (a.output/"README.md").write_text(readme,encoding="utf-8")
    return 1 if fails else 0
if __name__=="__main__":raise SystemExit(main())
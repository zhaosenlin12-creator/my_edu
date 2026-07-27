# VibeHub 鏈湴瀛︿範鎹曡幏

- 鏉ユ簮锛歨ttps://vibe-hub.org/
- Sitemap锛歨ttps://vibe-hub.org/sitemap.xml
- 鎶撳彇鏃ユ湡锛?026-07-27
- 鎶撳彇寮曟搸锛歋crapling锛堥粯璁わ紱鏈湴鏃犻渶 API key锛?- 鎶撳彇缁撴灉锛?84 椤癸紙涓枃 242 + 鑻辨枃 242锛夛紝澶辫触 0

## 涓夌浣跨敤鏂瑰紡

### 1. 鍦?Obsidian 閲屾绱紙鎺ㄨ崘鏃ュ父锛?
- 鍦?`pages/` 閲屾寜鐩綍璧拌锛涗腑鏂囧湪 `zh/`锛岃嫳鏂囧湪 `en/`
- 鐢?Excel 鎵撳紑 `index.csv`锛屾寜璇█銆佸垎绫汇€佹爣棰樼瓫閫?- 鎯虫壘涓婚褰掔被鏃舵墦寮€ `zh/topics/` 鎴?`en/topics/`锛圓I銆丅ackend銆丏esign銆丟it銆丳roduct銆乀echnology 鍏釜鍒嗙被绱㈠紩椤碉級

### 2. 鍦ㄦ祻瑙堝櫒閲屽儚鍘熺珯涓€鏍烽瑙堬紙鎺ㄨ崘浣撻獙锛?
`site/` 鏄畬鏁撮暅鍍忥紙HTML + CSS + JS + 鍥剧墖锛夛紝鍚姩鏈湴鏈嶅姟鍣ㄥ嵆鍙湪娴忚鍣ㄧ湅鍒颁笌 vibe-hub.org 涓€鑷寸殑椤甸潰銆佷氦浜掑拰鏍峰紡锛?
```powershell
python -m http.server 8765 --directory C:\my_know\70_Sources\vibe-hub\site
```

鐒跺悗娴忚鍣ㄦ墦寮€ <http://localhost:8765/>銆備腑鏂囩珯璧?`/`锛岃嫳鏂囩珯璧?`/en/`銆?
> 绗竴娆″惎鍔ㄩ暅鍍忚€楁椂 3-5 鍒嗛挓锛?84 椤?+ 532 璧勬簮銆傚悗缁嫢瑕佸埛鏂帮細
> ```powershell
> python C:\Users\Administrator\.codex\skills\website-knowledge-crawler\scripts\mirror_site.py `
>     https://vibe-hub.org C:\my_know\70_Sources\vibe-hub\site --workers 6
> ```

### 3. 璁?Codex 妫€绱紙鎺ㄨ崘 AI 杈呭姪锛?
姣忎釜 `pages/**/*.md` 閮芥槸娓呮磥鐨?Markdown锛屽墠缃?`type / source_url / title / language / category / engine / fetched_at`銆傚湪 Codex 閲岀洿鎺ヨ銆屽幓 70_Sources/vibe-hub 鎵?XX銆嶅嵆鍙储寮曟绱€?
## 瀛︿範璺嚎

鎸?[[50_AI/AI缂栫▼瀛︿範璺嚎]] 鐨勯『搴忚蛋锛屼笉寤鸿浠庡ご璇诲埌灏俱€傚厛鍋氬垎绫婚〉鐨勯€氳锛屽啀鎸夐渶閽诲崟鐐规湳璇€?
## 鎶撳彇涓庡悓姝?
- 鎶撳彇 skill锛歚website-knowledge-crawler`锛堜綅浜?`~/.codex/skills/website-knowledge-crawler/`锛?- 榛樿寮曟搸锛歋crapling锛堟湰鍦般€佹棤闇€ API key锛?- 澶囬€夊紩鎿庯細Firecrawl锛堥渶瑕?`FIRECRAWL_API_KEY` 涓?`FIRECRAWL_API_URL` 鐜鍙橀噺锛?- 鍏ㄩ噺鏇存柊锛圡arkdown锛夛細

  ```powershell
  python C:\Users\Administrator\.codex\skills\website-knowledge-crawler\scripts\crawl_site.py `
      https://vibe-hub.org C:\my_know\70_Sources\vibe-hub `
      --workers 4 --delay 0.15 --engine scrapling
  ```

- 鍏ㄩ噺闀滃儚锛圚TML锛夛細

  ```powershell
  python C:\Users\Administrator\.codex\skills\website-knowledge-crawler\scripts\mirror_site.py `
      https://vibe-hub.org C:\my_know\70_Sources\vibe-hub\site --workers 6
  ```

- 闅剧埇绔欑偣鍙敤 auto 寮曟搸鑷姩鍥為€€鍒?Firecrawl銆?
- `pages/` 宸茬撼鍏?git锛屽彲鍦?GitHub 浠撳簱鐪嬪埌瀹屾暣鎹曡幏鍐呭銆俙site/` 鍥犱綋绉緝澶т笉杩?git锛屾湰鍦版寜闇€鐢熸垚銆
---
type: web_source
source_url: "https://vibe-hub.org/en/upload"
title: "Upload"
language: en
category: "upload"
fetched_at: 2026-07-27T10:04:47+00:00
---
FrontendBackendProductTech StackAIGitDesign Styles

Copy as MarkdownCopied

←TimePickerForm→

# Upload

You might say

Let people upload their own images.

**Send a file from a device to the website**·Uploading includes choosing, transferring, and saving a file. Explain type, size, and count limits before selection, show progress during transfer, and allow retry after failure. The server still needs to check the file and the user's permission.

Know first

[Form](/en/form)

⬆Click or drag the file here*Supports JPG / PNG, no more than 10MB*

📄**Design Draft-Homepage.fig**66%

Upload**≠**[File](/en/file)

[Upload](/en/upload) handles choosing, transferring, and retrying a file. file displays a file that already exists or is being processed.

### When to use it

- Profile image

  ⬆ Drag files here, or click to choose
- Document attachment

  🖼🖼＋
- Import a data file

  📄 Requirements.docx✓

  📄 Design.fig66%
- Send media or project files

  ⬆ Click or drag to upload

  JPG and PNG supported, up to 10 MB each

### When NOT to use it

- Reveal limits only after a long upload fails

  Video URL⬆ Upload

  If people only have a URL, a text field is enough
- Show no progress for a large file

  🖼 IMG\_001.jpg12 / 38

  Uploading many small files one by one takes time and makes progress hard to manage
- Trust the filename or browser check as final validation

  📄 Video footage.mp4✕ Failed

  Without a retry option, people must upload again after failure
- Remove a failed file without offering a retry

  🎬 Final cut-4K.mp4 (1.8 GB)99%

  The size limit isn’t reported until the upload reaches 99%

Anatomy

⬆*Supports JPG / PNG, no more than 10MB*

📄**Design draft.fig**

1Drop ZoneA dashed area where users can drag files or click to select them

2HintState file-format and size limits up front

3File ItemOne file per row; users can remove and retry it

4File NameShows the file name

5ProgressClearly shows upload progress

Variants

Drag

⬆Drag the file here*or click to select*

When uploading large files or selecting files in batches

Button

⬆ Upload file

When space is limited, use a button to open the file picker

Picture

＋

When uploading an avatar or cover, the selected image needs to be displayed

List

📄**Requirements document.pdf**✓

📄**Design draft.fig**66%

When uploading multiple files, show each file’s progress separately.

Typical use cases

Avatar upload

![](/assets/avatar-fox.png)✎

**Avatar**

Supports JPG / PNG, no more than 2MB

Change avatar

Support attachment

**Submit a work order**

🖼**Problem screenshot.png**✓

📄**Log file.log**66%

CSV import

**Batch import members**
Download template

⬆Drag Excel / CSV here*or click to select the file, up to 500 rows at a time*

Cancel
Start import

Media library

I climbed Tanglang Mountain on the weekend and the sea of clouds was stunning 🌤

+

Publish

Further reading

[<input type="file">MDN ↗](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file)[HTML Drag and Drop APIMDN ↗](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API)

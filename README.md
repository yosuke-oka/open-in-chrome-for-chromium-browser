# Open in Chrome for Chromium Browser 

**This works only on macOS.**
A tiny extension that lets you **open the current tab in Google Chrome** — handy when you're using Arc / Brave / Vivaldi / Edge etc., but some pages (Google Workspace, SSO, internal tools) only work in Chrome.

Click the toolbar button → the same URL opens in Chrome.  
Nothing more, nothing less.

---

## Install

1. Download or clone this repo
2. Open `chrome://extensions`
3. Turn **Developer mode ON**
4. Click **Load unpacked**
5. Select this extension’s folder

### Native messaging setup (to launch Chrome)

1. Make the native script executable:

```
chmod +x ./native/open_in_chrome.py
```

2. Copy the messaging host config:

```
mkdir -p ~/Library/Application\ Support/Google/Chrome/NativeMessagingHosts
cp ./native/open_in_chrome.json ~/Library/Application\ Support/Google/Chrome/NativeMessagingHosts/
```

3. Edit `open_in_chrome.json` 
   - replace `<EXTENSION_ID>` with the ID shown on `chrome://extensions`
   - replace `<ABSOLUTE_PATH_TO_REPOSITORY>` with the absolute path to this repository
---

## Usage

Click the extension icon → the current page opens in **Google Chrome**.


chrome.action.onClicked.addListener(async () => {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  if (!tab?.url) return;

  chrome.runtime.sendNativeMessage(
    "open_in_chrome",
    { url: tab.url },
    () => { },
  );
});

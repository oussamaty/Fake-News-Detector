chrome.runtime.onInstalled.addListener(function() {
    chrome.storage.sync.set({BearerToken: 'AAAAAAAAAAAAAAAAAAAAAK1XJgEAAAAAekb17DbMiGVKBbXFsAS%2FAbyCU94%3D14Gs0GbX5GKlrDuEmC7Pk9USUIWl6MWKuPrYgDeXbKH0b23ASa'}, function() {
      });
    chrome.declarativeContent.onPageChanged.removeRules(undefined, function() {
        chrome.declarativeContent.onPageChanged.addRules([{
          conditions: [new chrome.declarativeContent.PageStateMatcher({
            pageUrl: {hostEquals: 'twitter.com'}
          })
          ],
              actions: [new chrome.declarativeContent.ShowPageAction()]
        }]);
      });
    chrome.pageAction.onClicked.addListener(function(tab) {
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs){
          
          chrome.tabs.sendMessage(tabs[0].id, {show:true});  
        });
    });
    chrome.runtime.onMessage.addListener((request,sender,sendResponse) => {
      if (request.tweet) {
        console.log(JSON.stringify(request));
        fetch(`http://localhost:5000/score?request=${JSON.stringify(request).replace(/&amp;/g,'/')}`).then((response) => response.json()).then((response) => {
        sendResponse({score:response.score});
        });
        return true;
      }
    })
  });
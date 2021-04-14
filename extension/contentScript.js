chrome.runtime.onMessage.addListener((response,sender,sendResponse) => {
  if (response.show) {
    show();
  }
  console.log('hhh');
  sendResponse({});
  return true;
});
function show() {
xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        let div = document.createElement('div');
        div.innerHTML = this.responseText;
        document.body.insertBefore(div, document.body.firstChild);
    }
};
xhttp.open("GET", chrome.runtime.getURL("/floating.html"), true);
xhttp.send();
click_phase = false;
chrome.storage.sync.get(['BearerToken'], function(data) {
  document.addEventListener('click',(e) => {
    if (e.target.outerHTML.indexOf('<img id="image-fermer"') == 0) {
      document.body.removeChild(document.body.firstChild);
      click_phase = false;
    } else {
      if (e.target.outerHTML == '<button class="button-floating ghost" id="start">Allons-y</button>') {
        document.getElementById('instructions').innerText = 'Veuillez cliquer sur le tweet à analyser';
        document.getElementById('start').style.display = 'none';
        document.getElementById('salut').style.display = 'none';
        click_phase = true;
      }
      const target = upTo(e.target,"article"); 
      let caught = true;
      let link = '';
      if (target){
      try{
        link = target.getElementsByTagName('a')[0].baseURI;
      } catch (error) {
        caught = false;
        if (error instanceof TypeError || link instanceof undefined) {
          link = '';
        } else {
          console.error(error);
        };
        document.getElementById('instructions').innerText = "Votre selection n'a pas été capturer, veuillez recliquer sur le tweet";
      };
      if (caught && click_phase) {
        document.getElementById('loading-animation').style.display = 'block';
        document.getElementById('instructions').style.display = 'none';
        document.getElementById('floating-panel').style.background = "linear-gradient(to right, #44C4A1, #32BEA6)"
        let scoreContainer = document.getElementById('score-container');
        if (scoreContainer) {
          scoreContainer.parentNode.removeChild(scoreContainer);
        }
        fetch('https://api.twitter.com/2/tweets/' + link.slice(link.indexOf("/status/") + 8) + "?expansions=author_id&tweet.fields=text,created_at,conversation_id,in_reply_to_user_id,referenced_tweets,public_metrics&user.fields=username,verified,public_metrics",{
          method:'GET',headers: {
            Authorization: `Bearer ${data.BearerToken}`,
            "Content-Type": "application/json"
          }
        }).then((tweet) => tweet.json()).then((tweet) => {
          result = {'id':tweet.data.id,'conversation_id':tweet.data.conversation_id,'date':tweet.data.created_at.replace("T", " ").split('.')[0],'tweet':tweet.data.text,'username':tweet.includes.users[0].username,'verified':tweet.includes.users[0].verified,'referenced_tweets':tweet.data.referenced_tweets,'in_reply_to_user_id':tweet.data.in_reply_to_user_id,'retweet_count':tweet.data.public_metrics.retweet_count,'reply_count':tweet.data.public_metrics.reply_count,'like_count':tweet.data.public_metrics.like_count,'geo':tweet.data.geo};
          chrome.runtime.sendMessage({tweet:result},(response) => {
            document.getElementById('loading-animation').style.display = 'none';
            scoreAnimation(parseFloat(response.score.toFixed(4))*100);
            click_phase = true;
          })

        });
      }
     }
    }
  });
});

upTo = (element, tagName) => {
  tagName = tagName.toLowerCase();
  while (element && element.parentNode) {
    element = element.parentNode;
    if (element.tagName && element.tagName.toLowerCase() == tagName) {
      return element;
    }
  }
  return null;
}

scoreAnimation = (score) => {
  document.getElementById('floating-panel').innerHTML += `<div id="score-container">
  <span id="score-display" data-unit="%"></span>
  <svg viewBox="0 0 100 100" id = "score-svg">
    <circle cx="50" cy="50" r="44" fill = "none" 	stroke-width="10"  id="score-osnova" />
    <circle  cx="50" cy="50" r="44" fill = "none" stroke-width="10" id="score-indicator" />
  </svg>
</div>`
  document.getElementById('score-display').innerText = score;
  var value = document.getElementById('score-display');
  var valueNumber = Number(value.innerText);
  var unitsMeasur = value.getAttribute("data-unit");

  var circleLength = document.getElementById("score-osnova").getTotalLength();

  var indicatorLength = (circleLength * valueNumber) / 100;
  document.getElementById('score-indicator').setAttribute("stroke-dasharray", indicatorLength + " " + circleLength);

  setTimeout(function() {
    document.getElementById('floating-panel').style.transition = 'background .5s;';
    document.getElementById('floating-panel').style.background = hsl_col_perc(score,120,0);
  }, 17);
  //counting animation
  var animDuration = 650;
  var countSpeed = animDuration / valueNumber;
  var step = 0;

  var runningСounter = setInterval(function () {
  value.innerHTML = step;
  step++;
  if (step > valueNumber) {
    clearInterval(runningСounter);
  }
}, countSpeed);
}
function hsl_col_perc(percent, start, end) {
  var a = percent / 100,
      b = (end - start) * a,
      c = b + start;

  // Return a CSS HSL string
  return 'hsl('+c+', 100%, 50%)';
}
}

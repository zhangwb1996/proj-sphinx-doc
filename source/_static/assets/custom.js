function time() {
  var timestamp = document.getElementById("timestamp");
  if (timestamp == null) {
    return;
  }
  var vWeek, vWeek_s, vDay;
  vWeek = ["星期天", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"];
  var date = new Date();
  year = date.getFullYear();
  month = date.getMonth() + 1;
  day = date.getDate();
  hours = date.getHours();
  minutes = date.getMinutes();
  seconds = date.getSeconds();
  vWeek_s = date.getDay();
  document.getElementById("timestamp").innerHTML =
    year +
    "年" +
    month +
    "月" +
    day +
    "日" +
    "\t" +
    hours +
    ":" +
    minutes +
    ":" +
    seconds +
    "\t" +
    vWeek[vWeek_s];
}
document.addEventListener("DOMContentLoaded", () => {
  // var htmlContext = document.querySelector('div[itemprop="articleBody"]');
  // var htmlContext = document.querySelector('div[itemprop="articleBody"]');
  var h1Context = document.querySelector('h1');
  if (h1Context != null) {
    h1Context.setAttribute('class', 'h1');
    h1Context.insertAdjacentHTML("beforebegin", `
    <small id = 'timestamp'></small>
    `
    )
    // var span = document.createElement("span")
    // h1Context.insertAdjacentElement("beforebegin", span)

    var timestamp = document.getElementById('timestamp');
    timestamp.insertAdjacentHTML("afterend", `
      <br>
      <small id = "ctime" ></small>&nbsp&nbsp
      <small id = "mtime"></small>
       `
    )
    var ctime = document.getElementById("ctime");
    var mtime = document.getElementById("mtime");
    ctime.innerHTML = document.getElementById("ctime-bak").innerText;
    mtime.innerHTML = document.getElementById("mtime-bak").innerText;

    time();
  }
});

setInterval("time()", 1000);

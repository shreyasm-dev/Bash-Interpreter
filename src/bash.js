function run(code) {
  var string = code.trimStart().split(" ")
  if (string[0] == 'echo') {
    var temparr = JSON.parse(JSON.stringify(string))
    temparr.shift()
    console.log(temparr.join(' '))
  } else if (string[0] == 'npm') {
    if (string.indexOf('i') != -1 || string.indexOf('install') != -1) {
      var temparr = JSON.parse(JSON.stringify(string))
      temparr.shift()
      temparr.shift()
      temparr = temparr.join(' ').trimStart().split(' ')
      console.log('Installed package ' + temparr.join(' '))
    } else if (string.indexOf('uninstall') != -1) {
      var temparr = JSON.parse(JSON.stringify(string))
      temparr.shift()
      temparr.shift()
      temparr = temparr.join(' ').trimStart().split(' ')
      console.log('Uninstalled package ' + temparr.join(' '))
    }
  }
}

# CoffeeScript file that should be compiled into main.js
SomeUsefulFunction = (msg) ->
  console.log(msg)

# document onReady BEGIN
$ ->
  hello = 'Hello World!'
  SomeUsefulFunction(hello)

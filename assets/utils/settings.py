import json, os

with open('./assets/config/local.min.json', 'r') as cnfFile: cnfStock=json.load(cnfFile)

def readjson(stock:json.load, where:str, what:str)->str|list|dict|int|float|tuple: 
    for word in stock[where]: return word[what]

geometry = readjson(cnfStock, 'app.data', 'app.data.geometry')
title = readjson(cnfStock, 'app.data', 'app.data.title')
framerate = readjson(cnfStock, 'app.data', 'app.data.framerate')

scale = readjson(cnfStock, 'app.engine', 'app.engine.scale')
outline = readjson(cnfStock, 'app.engine', 'app.engine.outline')

speed = readjson(cnfStock, 'app.player', 'app.player.speed')
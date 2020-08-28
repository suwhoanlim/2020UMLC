"""
Retrieved from http://codingdojang.com/scode/582
Written by 'justbegin' at 2018/02/18
Site visited at 2020/08/17
"""

import sympy as sp
from random import randint as ri
import json
from web3 import Web3



def inputdata(): # gets the point data for interpolation
    p = int(input('-> Enter the number of coordinates: '))
    data,x,y = [],0,0
    for i in range(p):
        x,y = map(float,input('').split())
        data.append([x,y])
    return data
 
'''
procudes a polynomial given a secret and a number of participants
1st var : secret integer
2nd var : number of participants

for n people of participants, n+1 degree polynomial will be produced

Rather than 
1) make poly that crosses (0,y) 
2) extract points from poly
this program goes
1) extract n points
2) make deg n poly with n+1 points
3) extract one more point from the poly
'''
def producepoly(): 
    sec = int(input('-> Enter the secret integer: '))
    num = int(input('-> Enter the number of shares you wish to create: '))
    points, ze, x, y = [], 0, 0, 0
    number = []
    points.append([ze,sec])
    """
    #Below line errors
    
    w = sp.Symbol('w')
    poly, fnc = 0, 1

    for i in range(num - 1):
        fnc *= w
        poly = ri(0, 100) * fnc
    
    for i in range(num):
        xval = ri(1, num + 100)
        while xval in number :
            xval = ri(1, num + 100)
        number.append(xval)
        points.append([xval, poly.subs(w, xval)])
    """
    
    for i in range(1, num):
        x = ri(1, num + 100)
        while x in number :
            x = ri(1, num + 100)
        number.append(x)
        y = ri(1, num + 100)
        points.append([x,y])
    L = whatsthepoly(points)
    
    print(sp.expand(L))
    tmp = ri(10, 20)
    x = sp.Symbol('x')
    tmpp = L.subs(x, tmp)
    points.append([tmp, tmpp])
    
    print(points)
    return points

'''
Performs Lagrange interpolation using the input data from inputdata()
'''
def whatsthepoly(data): # lagrange interpolation, input = points, output = polynomial
    n = len(data)
    x = sp.Symbol('x')
    y,L = 1,0
    for i in range(n):
        for h in range(n):
            if i == h:
                pass
            else:
                y *= (x-data[h][0])/(data[i][0]-data[h][0])
                # make an if-else statement here if you want to add an error case when denom = 0
        L += data[i][1]*y
        y = 1
    print(sp.expand(L))
    return L

'''
Given a set of data and polynomial L, the function evaluates the polynomial at point zero
'''
def whatsatzero(data, L):
    x = sp.Symbol('x')
    print(L.subs(x, 0))
    




if __name__ == "__main__":
    pointtt = producepoly()
    #data = inputdata()
    print(pointtt)

    L = whatsthepoly(pointtt)
    whatsatzero(pointtt, L)

    ganache_url = "http://127.0.0.1:7545"
    web3 = Web3(Web3.HTTPProvider(ganache_url))

    print(web3.isConnected())
    #account_1 = '0x09AE93c233Bf26b4f83824244d23c1A0EF61222D' # Fill me in
    #account_2 = '0xE96E7286bDa0AD5a22FA12c9a8E71380f33E125E' # Fill me in
    #private_key = '0x0ea6f4451dce5ab03185cdaf46b4bb66150720493ad97ba71f1319918b967af1' # Fill me in

    web3.eth.defaultAccount = web3.eth.accounts[0] # already unlocked

#    abi = json.loads('[{"inputs": [],"payable": false,"stateMutability": "nonpayable","type": "constructor"},{"constant": true,"inputs": [],"name": "greeting","outputs": [{"internalType": "string","name": "","type": "string"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": false,"inputs": [{"internalType": "uint256","name": "_x","type": "uint256"},{"internalType": "uint256","name": "_y","type": "uint256"}],"name": "setMap","outputs": [],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": true,"inputs": [{"internalType": "uint256","name": "_x","type": "uint256"}],"name": "getMap","outputs": [{"internalType": "uint256","name": "","type": "uint256"}],"payable": false,"stateMutability": "view","type": "function"}]')
    address = web3.toChecksumAddress("0x7aC457616849D7843098C8A93b70317Bf255DF01")

    abi = json.loads('[{"inputs": [],"payable": false,"stateMutability": "nonpayable", "type": "constructor"},{"constant": true,"inputs": [],"name": "greeting","outputs": [ {"internalType": "string","name": "","type": "string"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": false,"inputs": [],"name": "clearMap","outputs": [],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": false,"inputs": [{"internalType": "int256","name": "_x","type": "int256"},{"internalType": "int256","name": "_y","type": "int256"}],"name": "setMap","outputs": [],"payable": false,"stateMutability": "nonpayable","type": "function"}]')


    contract = web3.eth.contract(address = address, abi = abi)

    for i in range (1, len(pointtt)):
        tx_hash = contract.functions.setMap(pointtt[i][0], pointtt[i][1]).transact()
        web3.eth.waitForTransactionReceipt(tx_hash)
        print(i)
        #print('Updated mapping for', i, 'is: {}'.format(contract.functions.getMap(i).call()))
        




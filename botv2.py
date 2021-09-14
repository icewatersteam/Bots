from web3 import Web3
import os
from dotenv import load_dotenv
import asyncio
import time

load_dotenv()

infura = os.environ.get('WEB3_INFURA_PROJECT_ID')
w3 = Web3(Web3.HTTPProvider(f'https://ropsten.infura.io/v3/{infura}'))

gas_amount = 220000
walletAddress = os.getenv("BOT_ADDRESS_2")
walletPrivateKey = os.getenv("BOT_PRIVATE_KEY_2")

sleepPeriod = 300 #measured in seconds
#Heavy version
significantShift = 0.20
aggresion = 0.8

PRECISION = 10**18

waterAddress ='0xE9C2792ebBb0cFE78da0843d6bBfc05D84c7A2eb'
steamAddress = '0x8AE02fA7E819Db04E459C8B57909fd920b704b31'
iceAddress = '0xE38C9b65ca0B60cd857B010fDbF80503c4219A68'
controllerAddress = '0xd2355d3a05c0E51Fe765b7C4E084EcA42623f4F7'

tokenABI = [
    {
      "inputs": [],
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "spender",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "value",
          "type": "uint256"
        }
      ],
      "name": "Approval",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "from",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "value",
          "type": "uint256"
        }
      ],
      "name": "Transfer",
      "type": "event"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "spender",
          "type": "address"
        }
      ],
      "name": "allowance",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "spender",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "approve",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "balanceOf",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "value",
          "type": "uint256"
        }
      ],
      "name": "burn",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "decimals",
      "outputs": [
        {
          "internalType": "uint8",
          "name": "",
          "type": "uint8"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "spender",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "subtractedValue",
          "type": "uint256"
        }
      ],
      "name": "decreaseAllowance",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "spender",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "addedValue",
          "type": "uint256"
        }
      ],
      "name": "increaseAllowance",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "isController",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "value",
          "type": "uint256"
        }
      ],
      "name": "mint",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "name",
      "outputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "setController",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "symbol",
      "outputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "totalSupply",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "recipient",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "transfer",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "sender",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "recipient",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "transferFrom",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ]

controllerABI = [
    {
      "inputs": [
        {
          "internalType": "contract IceToken",
          "name": "iceToken",
          "type": "address"
        },
        {
          "internalType": "contract H2OToken",
          "name": "h2oToken",
          "type": "address"
        },
        {
          "internalType": "contract SteamToken",
          "name": "stmToken",
          "type": "address"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "account",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "string",
          "name": "tokenFrom",
          "type": "string"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amountFrom",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "string",
          "name": "tokenTo",
          "type": "string"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amountTo",
          "type": "uint256"
        }
      ],
      "name": "Swap",
      "type": "event"
    },
    {
      "inputs": [],
      "name": "calculateTargetIcePrice",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "claimH2OFromIce",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "claimableH2OFromIce",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "getChangeRate",
      "outputs": [
        {
          "internalType": "int256",
          "name": "",
          "type": "int256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "getColdH2OPoolSize",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "getICEPoolSize",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "getMeltRate",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "getSTMPoolSize",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "getWarmH2OPoolSize",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "dIceAmount",
          "type": "uint256"
        }
      ],
      "name": "previewSwapIceForWater",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "dSteamAmount",
          "type": "uint256"
        }
      ],
      "name": "previewSwapSteamForWater",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "dH2OAmount",
          "type": "uint256"
        }
      ],
      "name": "previewSwapWaterForIce",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "dH2OAmount",
          "type": "uint256"
        }
      ],
      "name": "previewSwapWaterForSteam",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "dIceAmount",
          "type": "uint256"
        }
      ],
      "name": "swapIceForWater",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "dSteamAmount",
          "type": "uint256"
        }
      ],
      "name": "swapSteamForWater",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "dH2OAmount",
          "type": "uint256"
        }
      ],
      "name": "swapWaterForIce",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "dH2OAmount",
          "type": "uint256"
        }
      ],
      "name": "swapWaterForSteam",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ]

controllerContract = w3.eth.contract(address = controllerAddress,abi = controllerABI)
waterContract = w3.eth.contract(address = waterAddress,abi = tokenABI)
steamContract = w3.eth.contract(address = steamAddress, abi = tokenABI)
iceContract = w3.eth.contract(address = iceAddress, abi = tokenABI) 

ice = iceContract.functions.balanceOf(walletAddress).call()
water = waterContract.functions.balanceOf(walletAddress).call()
steam = steamContract.functions.balanceOf(walletAddress).call()

#takes initial values
significant_ice = int(ice * significantShift)
significant_water = int(water * significantShift)
significant_steam = int(steam * significantShift)


def getPools():
    ice = controllerContract.functions.getICEPoolSize().call()
    coldWater = controllerContract.functions.getColdH2OPoolSize().call()
    steam = controllerContract.functions.getSTMPoolSize().call()
    warmWater = controllerContract.functions.getWarmH2OPoolSize().call()
    return ice,coldWater,steam,warmWater

def checkMelt():
    claimable = controllerContract.functions.claimableH2OFromIce().call()
    if claimable >= 100 * PRECISION:
        transaction = controllerContract.functions.claimH2OFromIce().buildTransaction(
            {'gas':gas_amount,
            'nonce': w3.eth.get_transaction_count(walletAddress)
            }
        )
        signed_tx = w3.eth.account.sign_transaction(transaction, walletPrivateKey)
        txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        w3.eth.wait_for_transaction_receipt(txn_hash)
        print("Withdrew " + str(claimable) + " H2O from melt")
    
def swapWatertoIce(amount):
    #approve
    transaction = waterContract.functions.approve(controllerAddress,amount).buildTransaction(
        {'gas':gas_amount,
        'nonce': w3.eth.get_transaction_count(walletAddress)
        }
    )
    
    signed_tx = w3.eth.account.sign_transaction(transaction, walletPrivateKey)
    txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    w3.eth.wait_for_transaction_receipt(txn_hash)
    #swap
    transaction = controllerContract.functions.swapWaterForIce(amount).buildTransaction(
        {'gas':gas_amount,
            'nonce': w3.eth.get_transaction_count(walletAddress)
            }
    )
    signed_tx = w3.eth.account.sign_transaction(transaction, walletPrivateKey)
    txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    return True

def swapIceToWater(amount):
    #approve
    transaction = iceContract.functions.approve(controllerAddress,amount).buildTransaction(
        {'gas':gas_amount,
            'nonce': w3.eth.get_transaction_count(walletAddress)
            }
    )
    signed_tx = w3.eth.account.sign_transaction(transaction, walletPrivateKey)
    txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    w3.eth.wait_for_transaction_receipt(txn_hash)
    #swap
    transaction = controllerContract.functions.swapIceForWater(amount).buildTransaction(
        {'gas':gas_amount,
            'nonce': w3.eth.get_transaction_count(walletAddress)
            }
    )
    signed_tx = w3.eth.account.sign_transaction(transaction, walletPrivateKey)
    txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    return True

def swapWaterToSteam(amount):
    #approve
    transaction = waterContract.functions.approve(controllerAddress,amount).buildTransaction(
        {'gas':gas_amount,
            'nonce': w3.eth.get_transaction_count(walletAddress)
            }
    )
    signed_tx = w3.eth.account.sign_transaction(transaction, walletPrivateKey)
    txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    w3.eth.wait_for_transaction_receipt(txn_hash)
    #swap
    transaction = controllerContract.functions.swapWaterForSteam(amount).buildTransaction(
        {'gas':gas_amount,
            'nonce': w3.eth.get_transaction_count(walletAddress)
            }
    )
    signed_tx = w3.eth.account.sign_transaction(transaction, walletPrivateKey)
    txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    return True

def swapSteamToWater(amount):
    #approve
    transaction = steamContract.functions.approve(controllerAddress,amount).buildTransaction(
        {'gas':gas_amount,
            'nonce': w3.eth.get_transaction_count(walletAddress)
            }
    )
    signed_tx = w3.eth.account.sign_transaction(transaction, walletPrivateKey)
    txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    w3.eth.wait_for_transaction_receipt(txn_hash)
    #swap
    transaction = controllerContract.functions.swapSteamForWater(amount).buildTransaction(
        {'gas':gas_amount,
            'nonce': w3.eth.get_transaction_count(walletAddress)
            }
    )
    signed_tx = w3.eth.account.sign_transaction(transaction, walletPrivateKey)
    txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    return True

def getBalances():
    ice = iceContract.functions.balanceOf(walletAddress).call()
    water = waterContract.functions.balanceOf(walletAddress).call()
    steam = steamContract.functions.balanceOf(walletAddress).call()
    return ice,water,steam

async def main():
    startingTime = time.time()
    runtime = ((float(input("How many hours would you like this program to run? (float)")) * 3600))
    endTime = startingTime + runtime
    print("Starting at EpochTime: "+str(startingTime))
    (prevIce,prevCold,prevSteam,prevWarm)= getPools()
    iteration = 0
    while (time.time() < endTime):
        iteration+=1
        print("Begining iteration "+ str(iteration)+", Time left: "+ str(endTime - time.time()))
        checkMelt()
        print("Begining delay ("+str(sleepPeriod)+" seconds)")
        await asyncio.sleep(sleepPeriod)
        print("Delay over, analyzing pools...")
        (postIce,postCold,postSteam,postWarm)= getPools()
        (iceBalance,waterBalance,steamBalance) = getBalances()
        #here, positive delta values signify a loss of that pool, negatives are a gain
        #we can get a % change by looking at ice's change over prevpool size, we then can counter this action to a degree?
        #should it be a % amount based on % change and balance or allow us to run out?
        deltaIce = prevIce - postIce
        deltaCold = prevCold - postCold
        deltaSteam = prevSteam - postSteam
        deltaWarm = prevWarm - postWarm
        #iceShift = abs(deltaIce) / prevIce
        #steamShift = abs(deltaSteam) / prevSteam
        print(f"Change in Ice: {deltaIce}, Change in ColdPool: {deltaCold}, Change in Steam: {deltaSteam}, Change in WarmPool: {deltaWarm}")
        if abs(deltaIce) > significant_ice:
            if deltaIce > 0: #provide ice
                potential = int(abs(deltaIce) * aggresion)
                if potential > iceBalance:
                    swapIceToWater(iceBalance - 100)
                else: swapIceToWater(potential)
            else: #buy ice
                potential = int(abs(deltaCold) * aggresion)
                
                if potential > waterBalance:
                    swapWatertoIce(waterBalance - 100)
                else: swapWatertoIce(potential)
        else: print("No singnificant ice shift")
        if abs(deltaSteam) > significant_steam:
            if deltaSteam > 0: #provide steam 
                potential = int(abs(deltaSteam) * aggresion)
                if potential > steamBalance:
                    swapSteamToWater(steamBalance - 100)
                else: swapSteamToWater(potential)
            else: #buy steam
                potential = int(abs(deltaWarm) * aggresion)
                if potential > waterBalance:
                    swapWaterToSteam(waterBalance - 100)
                else: swapWaterToSteam(potential)
        else: print("no significant steam shift")
        #Reset values for next time
        (prevIce,prevCold,prevSteam,prevWarm)= getPools()
    print("Program finished running, completed " + str(iteration) + " iterations.")
    
 


print("Establishing connection...")
if (w3.isConnected() != True): raise ConnectionError('Failed to connect to network')
print("Connected ")
asyncio.run(main())
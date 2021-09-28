from web3 import Web3
import os
from dotenv import load_dotenv
import asyncio
import time

load_dotenv()

infura = os.environ.get('WEB3_INFURA_PROJECT_ID')
w3 = Web3(Web3.HTTPProvider(f'https://ropsten.infura.io/v3/{infura}'))

gas_amount = 300000 #ok for now, might need adjusting
walletAddress = os.getenv("BOT_ADDRESS_1")
walletPrivateKey = os.getenv("BOT_PRIVATE_KEY_1")

sleepPeriod = 250 #measured in seconds
minIceBuy = 10 # will wait until it can buy this many ice

PRECISION = 10**18

waterAddress =os.getenv("WATER")
steamAddress = os.getenv("STEAM")
iceAddress = os.getenv("ICE")
controllerAddress = os.getenv("CONTROLLER")

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
          "indexed": False,
          "internalType": "uint256",
          "name": "timestamp",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "icePoolSize",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "coldH2OPoolSize",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "warmH2OPoolSize",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "stmPoolSize",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "icePrice",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "stmPrice",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "targetIcePrice",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "int256",
          "name": "changeRate",
          "type": "int256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "iceTotalSupply",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "h2oTotalSupply",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "stmTotalSupply",
          "type": "uint256"
        }
      ],
      "name": "HistoryEvent",
      "type": "event"
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
      "name": "getICEPoolSize",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function",
      "constant": True
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
      "type": "function",
      "constant": True
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
      "type": "function",
      "constant": True
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
      "type": "function",
      "constant": True
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
      "type": "function",
      "constant": True
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
      "type": "function",
      "constant": True
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
      "type": "function",
      "constant": True
    },
    {
      "inputs": [],
      "name": "getIcePrice",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function",
      "constant": True
    },
    {
      "inputs": [],
      "name": "getSteamPrice",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function",
      "constant": True
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
      "type": "function",
      "constant": True
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
      "type": "function",
      "constant": True
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
      "type": "function",
      "constant": True
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
      "type": "function",
      "constant": True
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
      "type": "function",
      "constant": True
    }
  ]

controllerContract = w3.eth.contract(address = controllerAddress,abi = controllerABI)
waterContract = w3.eth.contract(address = waterAddress,abi = tokenABI)
steamContract = w3.eth.contract(address = steamAddress, abi = tokenABI)
iceContract = w3.eth.contract(address = iceAddress, abi = tokenABI) 

#checks every 5-10 minutes on if there is a shift in pool size
#counters all steam txs, counters ice tx if moved away from stablizing
#after doing its own tx updates amounts to not counter itself
#how to deal with balances? maybe % of balance used to counter is dependent on the size of the pool change



def getPools():
    ice = controllerContract.functions.getICEPoolSize().call()
    coldWater = controllerContract.functions.getColdH2OPoolSize().call()
    steam = controllerContract.functions.getSTMPoolSize().call()
    warmWater = controllerContract.functions.getWarmH2OPoolSize().call()
    return ice,coldWater,steam,warmWater

def checkMelt():
    claimable = controllerContract.functions.claimableH2OFromIce().call({'from':walletAddress})
    print("H2O melted: "+str(claimable))
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
        
        print("Begining delay ("+str(sleepPeriod)+" seconds)")
        await asyncio.sleep(sleepPeriod)
        checkMelt()
        print("Delay over, analyzing...")
        #(postIce,postCold,postSteam,postWarm)= getPools()
        (iceBalance,waterBalance,steamBalance) = getBalances()
        #print(f"Change in Ice: {deltaIce}, Change in ColdPool: {deltaCold}, Change in Steam: {deltaSteam}, Change in WarmPool: {deltaWarm}")
        icePrice = controllerContract.functions.getIcePrice().call()
        if ((icePrice * minIceBuy) < waterBalance):
          swapWatertoIce(waterBalance - 100)
          print("bought ice")
        #Reset values for next time
        #(prevIce,prevCold,prevSteam,prevWarm)= getPools()
    print("Program finished running, completed " + str(iteration) + " iterations.")
    
 


print("Establishing connection...")
if (w3.isConnected() != True): raise ConnectionError('Failed to connect to network')
print("Connected ")
asyncio.run(main())
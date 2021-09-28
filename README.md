# Bots
Bots to interact with the IceWater ecosystem

To run this program you will need a few things:

**Infura project ID** (API token), this is available for free on infura.io, save this as a system enviromental variable or in the .env file which we will use. It can handle up to 100,000 calls a day with the free ID.

**Ethereum wallet address and private key** These we will also store in the .env, add the .env file to a .gitignore to keep the wallets credential's safe.

These bots was made for the Icewater contracts begining 9/13/21, if the contracts source code doesn't change much then the ABI's won't need updating; otherwise new ABI's should be aquired. Make sure the addresses are up to date **(the addresses have been migrated to the .env in later versions)**, along with appropriate gas values. By default, an average gas price will be used when sending the transactions, this can also be specified by adding 'gasPrice': VALUE inside the curly brackets in the buildTransaction function. VALUE should be an integer measured in wei. 

Run like any other Python file: 
$ python bot____.py

Many values can be changed and customized, to make your own strategy follow along with the while loop in the main() function and tinker with whatever you like!

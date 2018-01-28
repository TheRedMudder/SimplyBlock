# SimplyBlock
SimplyBlock is a simple Blockchain project that stores randomly generated user transactions into blocks. It only uses the built-in python modules. 
## Getting Started

Download Python 3 https://www.python.org/downloads/
Download/Clone this repo
Open CMD/Terminal in the project directory and run python block.py to generate the blockchain

## Examples
Generating a new blockchain:
```
simplyBlockContent={'blockIndex':0,'lasthash': None,'useract':[userAccount],"txn":[None]}
simplyBlock={'hash':getHash(simplyBlockContent),'block':simplyBlockContent}
simplyChain=[simplyBlock]
```
Opening Existing:
```
with codecs.open('simplyblock.json', 'r') as outfile:#Using codecs.open instead of open b/c of errors in certain encodings
	simplyChain=json.load(outfile)
```



<img align="right" src="https://i.imgur.com/BeS5rfh.png" width=15%>

# SimplyBlock
SimplyBlock is a simple Blockchain project that stores randomly generated user transactions into blocks. It only uses the built-in python modules. 
## Getting Started

* Download [Python 3](https://www.python.org/downloads/)
* Download/Clone the repo
* Open CMD/Terminal in the project directory and run `python block.py` to generate the blockchain
* The Blockchain will save to `simplyblock.json`
## Examples
Generating a new blockchain:
```python
simplyBlockContent={'blockIndex':0,'lasthash': None,'useract':[userAccount],"txn":[None]}
simplyBlock={'hash':getHash(simplyBlockContent),'block':simplyBlockContent}
simplyChain=[simplyBlock]
```
Opening existing blockchain:
```python
with codecs.open('simplyblock.json', 'r') as outfile:
	simplyChain=json.load(outfile)
```
Create transaction to process(John sends Ron 57 units):
```python
transactionToProcess = [{'reciever':'Ron','sender':'John','amount':57}]
```
Generate random transactions to process:
```python
transactionToProcess = generateTransactions(userAccount,15)
```
Process transactions to new block:
```python
simplyChain.append(processTransactionsToBlock(userAccount,simplyChain,transactionToProcess))
userAccount=getUpdatedUserAccount()
```
Print last block:
```python
print(simplyChain[-1])
```
Print entire chain:
```python
print(simplyChain)
```
Verify Transaction(returns True if Valid, False if Invalid)
```python
verifyTransaction(transaction, userAccount)
```

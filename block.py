import hashlib,random,codecs,json
userAccount={'Ron':50,'John':50,'Paul':50} #Initial Users and Account Balance
def getHash(info=""):
    return hashlib.sha3_256(str(info).encode('utf-8')).hexdigest()#Returns hash for block content
def generateTransaction(userAccount):#Random Transactions(The invalid ones will not be added to the Block)
    try:
        usernum = random.sample(range(1, len(userAccount) + 1), 2)  # Generates 2 numbers from 1 to total user accounts
    except:
        print("ERROR: 'userAccount' needs at least two users.")#This only occurs if len(userAccount)<2
    currentuser=1#Randomly picks Senders and Recievers based on usernum
    for user in userAccount:
        if (currentuser==usernum[0]):
            reciever=user
        if (currentuser==usernum[1]):
            sender=user
        currentuser+=1
    return {'reciever':reciever,'sender':sender,'amount':random.randint(1,50)}
def generateTransactions(userAccount,count):
    return [generateTransaction(userAccount) for i in range(count)]#Calls above function 'count' amount of times
def verifyTransaction(trans,userAccount):
    requiredusers = (trans["sender"], trans["reciever"])
    if all(user in userAccount for user in requiredusers):#Check if sender/reciever exist
        senderBalance=userAccount[trans['sender']]
        transferAmount=trans['amount']
        return not (senderBalance-transferAmount<0)#True if sender has enough Balance
    else:
        return False#User doesn't exist
def applyTransaction(trans,userAccount):
    userAccount=userAccount.copy()#Required before making changes
    transferAmount = trans['amount']
    userAccount[trans['sender']] = userAccount[trans['sender']]-transferAmount #subtract Sender Balance
    userAccount[trans['reciever']] = userAccount[trans['reciever']]+transferAmount# Add Reciever Balance
    return userAccount
def newBlock(userAccount,simplyChain,txn):#creates new block
    lastBlock=simplyChain[-1]#gets last block
    simplyBlockContent = {'blockIndex': lastBlock['block']['blockIndex']+1, 'lasthash': lastBlock['hash'], 'useract': [userAccount],"txn":txn}
    simplyBlock = {'hash': getHash(simplyBlockContent), 'block': simplyBlockContent}
    return simplyBlock
def getUpdatedUserAccount():#Gets UserAccount Info from Block
    lastBlock=simplyChain[-1]#gets last block
    return lastBlock['block']['useract'][0]
def processTransactionsToBlock(userAccount,simplyChain,transactionToProcess):
    userAccount=userAccount.copy()#Required before making changes
    txn = []#Valid Transactions will be added to this variable
    txn_invalid = 0#Count Invalid Transactions
    for transaction in transactionToProcess:
        if verifyTransaction(transaction, userAccount):#Apply only if verified
            userAccount = applyTransaction(transaction, userAccount)
            txn.append(transaction)
        else:
            txn_invalid += 1
    print("Processed:"+str(len(transactionToProcess)-txn_invalid) +", Skipped Transactions: " + str(txn_invalid))
    makeBlock=newBlock(userAccount,simplyChain,txn)#Create block
    return makeBlock

#Either import existing block or create First Block
try:#try to import
    with codecs.open('simplyblock.json', 'r') as outfile:#Using codecs.open instead of open b/c of errors in certain encodings
        simplyChain=json.load(outfile)
except:#Except most likely caused by file not existing, but I'll just catch all errors to handle corrrupt files
    simplyBlockContent={'blockIndex':0,'lasthash': None,'useract':[userAccount],"txn":[None]}
    simplyBlock={'hash':getHash(simplyBlockContent),'block':simplyBlockContent}
    simplyChain=[simplyBlock]

print("Chain Created:"+str(simplyChain)+"\n");

#Generate 15 Transactions for Processing
transactionToProcess = generateTransactions(userAccount,15)
#Process Transactions to Block
simplyChain.append(processTransactionsToBlock(userAccount,simplyChain,transactionToProcess))
userAccount=getUpdatedUserAccount()

print("Block#"+str(simplyChain[-1]['block']['blockIndex'])+ " Added:"+str(simplyChain[-1])+"\n")
print("The orignal user account was:"+str(simplyChain[0]['block']['useract'][0])+", but now is:"+str(userAccount))


print("Let's add another Block the same way.")
#Same Code as above for Block
transactionToProcess = generateTransactions(userAccount,55)
simplyChain.append(processTransactionsToBlock(userAccount,simplyChain,transactionToProcess))
userAccount=getUpdatedUserAccount()
#Save Chain locally
with codecs.open('simplyblock.json', 'w') as outfile:#Using codecs.open instead of open b/c of errors in certain encodings
    json.dump(simplyChain, outfile)
print("Saved Blockchain locally")
print("The block size is: "+str(simplyChain[-1]['block']['blockIndex'])+". The current accounts balances are:"+str(userAccount)+". Rerun script to see blocks added.")

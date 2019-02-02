# Unchained Ledger
## What is it?
Unchained Ledger is a distributed ledger with a limited number of verifiers that is robust against double spending attacks without using the blockchain mechanism in the sense of creating a number of blocks and chaining them together. 

Unchained Ledger is designed to maximize simplicity so that any developer can easily check all its codes and see how it works.
## How does it work?
Suppose we have 101 verifiers and all end users have their IP addresses and public keys.
### Scenario 1: What happens most of the time
- Alice wants to send some tokens to Bob.
- She signs a request to reduce her account balance and induce Bob’s. 
- She then informs all the 101 nodes of her request and sends Bob the transaction hash.
- Bob’s client checks the transaction in all the nodes. 
- If all the nodes verify the transaction, it is verified and Bob delivers what he has promised Alice.
### Scenario 2: Alice double spends but Bob receives tokens
- Alice decides to double spend. She makes two transactions with the same nonce. One sends tokens to Bob and the other one sends tokens to another address that might be her own. 
- She informs 51 nodes about one of the transactions that sends tokens to Bob and tells the remaining 50 nodes about the other one.
- She sends Bob the transaction hash.
- Bob’s client checks the transaction in all nodes and quickly realizes that there’s another transaction with the same nonce, and Alice has double spent.
- Bob halts delivering what he has promised Alice. 
- The majority of nodes have received the transaction that sends Bob the tokens. 
- Bob’s client receives signatures from 51 nodes and asks the other 50 to update their ledgers.
- Those 50 nodes save the signatures of the other 51 and update their ledger.
- When Bob’s client receives signatures from all 101 nodes and they all verify the transaction, he is ensured that the transaction has been finalized and delivers what he has promised to Alice.
### Scenario 3: Alice double spends but does not receive what Bob promised her
- Alice decides to double spend. She makes two transactions with the same nonce. One sends tokens to Bob and the other one sends tokens to another address that might be her own.
- She informs 50 nodes about one of the transactions that sends tokens to Bob and tells the remaining 51 nodes about the other one.
- Bob’s client is informed of the double spend by realizing that 51 (the majority) nodes have registered a different transaction.
- Bob does not deliver what he has promised to Alice. 
### Scenario 4: Some nodes are down
- Bob’s client does not receive a double spend report from any nodes that are on and respond. Not even one of them.
- However, some of the nodes do not respond at all due to shutdown, network problems, etc.
- If at least 51 nodes are on and verify the registration of the transaction, Bob is ensured and sends Alice what he has promised.
- Bob’s client periodically tries to inform the other non-responding nodes and ask them to update their ledger in case they have another version of it.
### Scenario 5: Alice attacks the network to break the sync I 
- Alice tries to create a state for the network so that it can not sync.
- She informs 30 nodes about sending tokens to Bob, tells another 30 nodes about sending the same tokens to Chad, and claims about sending the tokens to David for the remaining 41 tokens.
- David’s client lists the signatures of all nodes signifying what transaction they have received. It then announces the list of all transactions and signatures to 60 nodes who have registered different transactions.
- The transaction that sends David the tokens has signatures from more nodes than the other two transactions, so after viewing the complete list of transactions all nodes update their ledger to that transaction.
### Scenario 6: Alice attacks the network to break the sync II
- Alice tries to create a state for the network so that it can not sync.
- She informs 40 nodes about sending tokens to Bob, tells another 40 about sending the same tokens to Chad, and claims about sending the tokens to David for the remaining 31 tokens.
- All their clients realize they have received a transaction. But when they ask for nodes’ signatures, they realize not all nodes verify their transaction.
- David’s client cannot finalize the transaction for itself.
- When some transactions have signatures from an equal number of nodes, the transaction with the minimum hash will be accepted by all nodes.
- Chad’s client realizes it has an equal number of signatures from nodes compared to Bob. But, his transaction hash is lower than Bob’s.
- Chad’s client creates a list of all transactions and signatures and makes all nodes update their ledger to include Chad’s transaction.
## Principles
- Nodes DO NOT relay transactions they receive to other nodes in the network. Senders are responsible for sending transactions to all nodes and receivers are responsible for asking for nodes’ verification. 
- Each node registers a transaction with a specific nonce from an address unless it has not received a transaction with earlier nonce yet or it has already registered another transaction with the same nonce. It does not need to inquire from other nodes.
- Nodes update their ledger and replace the transaction with a new one only if they receive a list that demonstrates the state of other nodes and proves what state they will sync to.    
- If receivers come upon even a single node with a different transaction, they will refrain from delivering what they have promised until that node updates its ledger and verifies that transaction. 
- When senders double spend and send tokens to several addresses, the receiver that has the signature from the majority and can update all the network to its benefit will actively sync all the network into a unified state.
- The state of not being sync creates no problem for any of the players except for the sender who has double spent. Because his account balance is reduced and none of the receivers will deliver what they have promised until the network is synchronized.
- Creating the list of all transactions and signatures and syncing all the nodes whenever the network is out of sync can be done by other players besides clients. If none of the clients sync the network to their own benefit in due time, other synchronizers can exist to observe the network and sync it to a unified state for each transaction.


## How to launch: 
#### Unchained Ledger is still under development and has not been fully implemented yet.

```shell
git clone https://github.com/ideal-money/unchained-ledger.git

cd unchained-ledger

virtualenv -p python3.6 venv
. venv/bin/activate

# Just for first time
pip install -e .
export FLASK_APP=node
export FLASK_ENV=development

# For running app, type this command
flask run
```

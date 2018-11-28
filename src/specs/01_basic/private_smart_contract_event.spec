# Private smart contract with event

 Tags: basic

Log events in total are only available in participated parties.
A private smart contract, `ClientReceipt`, logs all the deposits that have been performed.
```
pragma solidity ^0.4.0;

contract ClientReceipt {
    event Deposit(
        address indexed _from,
        bytes32 indexed _id,
        uint _value
    );

    function deposit(bytes32 _id) public payable {
        emit Deposit(msg.sender, _id, msg.value);
    }
}
```

## Log events in total are **only** captured in participated parties when executing the contract

 Tags: event, log

* Deploy `ClientReceipt` smart contract from a default account in "Node1" and it's private for "Node7", named this contract as "contract17"
* "contract17" is mined
* Execute "contract17"'s `deposit()` function "10" times with arbitrary id and value from "Node1". And it's private for "Node7"
* "Node1" has received "10" transactions which contain "10" log events in total
* "Node7" has received "10" transactions which contain "10" log events in total
* "Node2" has received "10" transactions which contain "0" log events in total
* "Node3" has received "10" transactions which contain "0" log events in total
* "Node4" has received "10" transactions which contain "0" log events in total
* "Node5" has received "10" transactions which contain "0" log events in total
* "Node6" has received "10" transactions which contain "0" log events in total


## Log events in the state are **only** captured in participated parties when executing the contract

 Tags: event, log

* Deploy `ClientReceipt` smart contract from a default account in "Node1" and it's private for "Node2", named this contract as "contract12"
* "contract12" is mined
* Deploy `ClientReceipt` smart contract from a default account in "Node2" and it's private for "Node3", named this contract as "contract23"
* "contract23" is mined
* Deploy `ClientReceipt` smart contract from a default account in "Node3" and it's private for "Node4", named this contract as "contract34"
* "contract34" is mined
* Deploy `ClientReceipt` smart contract from a default account in "Node4" and it's private for "Node5", named this contract as "contract45"
* "contract45" is mined
* Deploy `ClientReceipt` smart contract from a default account in "Node5" and it's private for "Node6", named this contract as "contract56"
* "contract56" is mined
* Deploy `ClientReceipt` smart contract from a default account in "Node6" and it's private for "Node7", named this contract as "contract67"
* "contract67" is mined
* Deploy `ClientReceipt` smart contract from a default account in "Node7" and it's private for "Node1", named this contract as "contract71"
* "contract71" is mined
* Execute "contract12,contract23,contract34,contract45,contract56,contract67,contract71"'s `deposit()` function "10" times with arbitrary id and value between original parties
* "Node1" has received transactions from "contract12" which contain "10" log events in state
* "Node2" has received transactions from "contract12" which contain "10" log events in state
* "Node2" has received transactions from "contract23" which contain "10" log events in state
* "Node3" has received transactions from "contract23" which contain "10" log events in state
* "Node3" has received transactions from "contract34" which contain "10" log events in state
* "Node4" has received transactions from "contract34" which contain "10" log events in state
* "Node4" has received transactions from "contract45" which contain "10" log events in state
* "Node5" has received transactions from "contract45" which contain "10" log events in state
* "Node5" has received transactions from "contract56" which contain "10" log events in state
* "Node6" has received transactions from "contract56" which contain "10" log events in state
* "Node6" has received transactions from "contract67" which contain "10" log events in state
* "Node7" has received transactions from "contract67" which contain "10" log events in state
* "Node7" has received transactions from "contract71" which contain "10" log events in state
* "Node1" has received transactions from "contract71" which contain "10" log events in state

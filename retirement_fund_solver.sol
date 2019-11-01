pragma solidity ^0.4.21;

contract SelfDestruct {
	function SelfDestruct() public payable {
		require(msg.value > 0);
	}

	function kill(address _target) public {
		selfdestruct(_target);
	}
}

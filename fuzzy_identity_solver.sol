pragma solidity ^0.4.21;

import "fuzzy_identity.sol";

/*
interface IName {
	function name() external view returns (string) {}
}
*/

contract returnSmarx is IName {
	function name() public view returns (bytes32) {
		return bytes32("smarx");
	}

	function exploit(address _addr) public {
		FuzzyIdentityChallenge c = FuzzyIdentityChallenge(_addr);
		c.authenticate();
	}
}

contract returnAddress {
	function keccakHash(address _addr, uint8 nonce) public returns (address) {
		return address(keccak256(0xd6, 0x94, _addr, nonce));
	}
}

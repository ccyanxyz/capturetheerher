pragma solidity ^0.4.24;

contract returnAddress {
	function keccakHash(address _addr, uint8 nonce) public view returns (address) {
		return address(keccak256(0xd6, 0x94, _addr, nonce));
	}
}

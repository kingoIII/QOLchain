// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract QOLClaimNFT is ERC721 {
    constructor() ERC721("QOL Claim", "QOLC") {}

    function mint(address to, uint256 tokenId) external {
        _mint(to, tokenId);
    }
}

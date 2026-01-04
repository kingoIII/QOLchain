import { ethers } from 'ethers';

// Mint a QOLClaimNFT token. Configure PROVIDER_URL and CONTRACT_ADDRESS.
// Usage: ts-node scripts/mintNFT.ts <privateKey> <to> <tokenId>

const PROVIDER_URL = process.env.PROVIDER_URL || '';
const CONTRACT_ADDRESS = process.env.QOL_NFT_ADDRESS || '';
const ABI = ["function mint(address,uint256) external"];

const args = process.argv.slice(2);
if (args.length < 3) {
  console.error('Usage: <privateKey> <to> <tokenId>');
  process.exit(1);
}

(async () => {
  const [privateKey, to, tokenId] = args;
  const provider = new ethers.providers.JsonRpcProvider(PROVIDER_URL);
  const wallet = new ethers.Wallet(privateKey, provider);
  const contract = new ethers.Contract(CONTRACT_ADDRESS, ABI, wallet);

  const tx = await contract.mint(to, tokenId);
  console.log('tx hash:', tx.hash);
  await tx.wait();
  console.log('minted');
})();

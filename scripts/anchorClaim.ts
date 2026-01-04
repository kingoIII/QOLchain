import { ethers } from 'ethers';

// Anchor a claim hash on-chain. Configure PROVIDER_URL and CONTRACT_ADDRESS.
// Usage: ts-node scripts/anchorClaim.ts <privateKey> <claimHash>

const PROVIDER_URL = process.env.PROVIDER_URL || '';
const CONTRACT_ADDRESS = process.env.QOL_ANCHOR_ADDRESS || '';
const ABI = ["function anchor(bytes32) external"];

const args = process.argv.slice(2);
if (args.length < 2) {
  console.error('Usage: <privateKey> <claimHash>');
  process.exit(1);
}

(async () => {
  const [privateKey, claimHash] = args;
  const provider = new ethers.providers.JsonRpcProvider(PROVIDER_URL);
  const wallet = new ethers.Wallet(privateKey, provider);
  const contract = new ethers.Contract(CONTRACT_ADDRESS, ABI, wallet);

  const tx = await contract.anchor(claimHash);
  console.log('tx hash:', tx.hash);
  await tx.wait();
  console.log('anchored');
})();

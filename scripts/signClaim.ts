import { Wallet } from 'ethers';

// Sign a claim hash with a private key
// Usage: ts-node scripts/signClaim.ts <privateKey> <claimHash>

const args = process.argv.slice(2);
if (args.length < 2) {
  console.error('Usage: <privateKey> <claimHash>');
  process.exit(1);
}

const [privateKey, claimHash] = args;
const wallet = new Wallet(privateKey);

(async () => {
  const sig = await wallet.signMessage(Buffer.from(claimHash.replace(/^0x/, ''), 'hex'));
  console.log('signature:', sig);
  console.log('signer:', wallet.address);
})();

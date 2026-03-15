#!/usr/bin/env tsx
/**
 * ZAK CLI entry point.
 *
 * Run with: npx tsx bin/zak.ts <command>
 * Or via package.json: npm run cli -- <command>
 */

import { runCli } from "../src/cli/main.js";

runCli();

// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from 'next'
import {PrismaClient} from "@prisma/client"

const prisma = new PrismaClient()

export  default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  
  const pings = await  prisma.ping.findMany();
  res.status(200).json(JSON.parse(JSON.stringify(pings)))
}

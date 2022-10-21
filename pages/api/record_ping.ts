// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from 'next'
import {PrismaClient} from "@prisma/client"

const prisma = new PrismaClient()

type Data = {
  name: string
}

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<Data>
) {

  const query = req.query;
  const { deviceId } = query;
  
  await prisma.ping.create({
    data:{
      deviceId: deviceId as string  
    }
  })

  res.status(200)
}

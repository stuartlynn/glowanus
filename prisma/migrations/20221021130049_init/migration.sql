-- CreateTable
CREATE TABLE "Ping" (
    "id" SERIAL NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "deviceId" VARCHAR(255) NOT NULL,

    CONSTRAINT "Ping_pkey" PRIMARY KEY ("id")
);

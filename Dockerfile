FROM node:20-alpine

WORKDIR /app

COPY package.json .
# Если нет package-lock.json, устанавливаем зависимости так:
RUN npm install

COPY . .

CMD ["npm", "run", "dev"]
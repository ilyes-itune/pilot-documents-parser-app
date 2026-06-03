FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build

FROM node:18-alpine
WORKDIR /app
RUN npm install -g http-server
COPY --from=0 /app/dist/pilot-documents-parser ./dist/pilot-documents-parser

EXPOSE 4200

CMD ["http-server", "dist/pilot-documents-parser", "-p", "4200", "--gzip"]

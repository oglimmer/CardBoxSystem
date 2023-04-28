FROM node:18 as builder

WORKDIR /opt/build

COPY . /opt/build

RUN npm i && npm run build

FROM nginx

COPY --from=builder /opt/build/dist /usr/share/nginx/html

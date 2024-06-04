# Dockerfile for Vue frontend

FROM node:14

# Set working directory
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy project files
COPY . .

# Copy the production environment file
COPY .env.production .env

# Build the project
RUN npm run build

# Expose the port and start the application
EXPOSE 8080
CMD ["npm", "run", "serve"]

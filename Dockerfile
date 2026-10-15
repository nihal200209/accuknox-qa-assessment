FROM alpine:latest

# Install necessary packages (bash, netcat, fortune, etc., depending on script requirements)
RUN apk update && apk add --no-cache bash fortune cowsay netcat-openbsd

# Set working directory
WORKDIR /app

# Copy application source code
COPY . /app

# Expose the application port (typically 4499 for Wisecow)
EXPOSE 4499

# Make script executable if needed
RUN chmod +x wisecow.sh

# Run the application
CMD ["./wisecow.sh"]
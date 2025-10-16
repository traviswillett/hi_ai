# Use the official Jekyll image with Ruby
FROM jekyll/jekyll:4.2.2

# Set the working directory
WORKDIR /srv/jekyll

# Copy the Gemfile if it exists, otherwise Jekyll will use defaults
COPY Gemfile* ./

# Install dependencies
RUN bundle install

# Expose the port Jekyll runs on
EXPOSE 4000

# Default command to serve the site
CMD ["jekyll", "serve", "--host", "0.0.0.0", "--livereload", "--incremental", "--force_polling"]
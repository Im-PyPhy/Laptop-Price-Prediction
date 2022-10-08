mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
<<<<<<< HEAD
" > ~/.streamlit/config.toml
=======
" > ~/.streamlit/config.toml
>>>>>>> 601b9950a241bc7721af0ebd6105c9a47eea32b1

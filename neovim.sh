NVIM_LISTEN_ADDRESS=/tmp/nvim ./nvim

#./nvim -c ":redir! >address.txt | :echo $NVIM_LISTEN_ADDRESS | :redir END | :q"
#./nvim -c ":redir! >address.txt" -c ":echo $NVIM_LISTEN_ADDRESS" -c ":redir END" -c ":q"
#cat address.txt

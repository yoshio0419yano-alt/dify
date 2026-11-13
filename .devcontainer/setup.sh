# --- Docker をディスク節約構成に切り替え ---
sudo mkdir -p /etc/docker
cat <<'EOF' | sudo tee /etc/docker/daemon.json
{
  "features": { "containerd-snapshotter": false },
  "log-driver": "json-file",
  "log-opts": { "max-size": "10m", "max-file": "3" }
}
EOF

sudo pkill dockerd || true
sleep 3
sudo rm -rf /var/lib/docker/containerd
sudo /usr/local/share/docker-init.sh
sleep 10
docker info | grep -i "storage driver"

#!/usr/bin/env python3
import sys
import struct
import json
import subprocess


def read_message():
  # 先頭4バイト: メッセージ長 (little endian)
  raw_length = sys.stdin.buffer.read(4)
  if len(raw_length) == 0:
    return None

  msg_length = struct.unpack("<I", raw_length)[0]
  if msg_length == 0:
    return None

  message_bytes = sys.stdin.buffer.read(msg_length)
  if len(message_bytes) == 0:
    return None

  return json.loads(message_bytes.decode("utf-8"))


def send_message(msg: dict):
  data = json.dumps(msg).encode("utf-8")
  sys.stdout.buffer.write(struct.pack("<I", len(data)))
  sys.stdout.buffer.write(data)
  sys.stdout.buffer.flush()


def main():
  msg = read_message()
  if not msg:
    return

  url = msg.get("url")
  if url:
    # mac の Google Chrome で URL を開く
    subprocess.run(["open", "-a", "Google Chrome", url])

  # 軽い OK レスポンスだけ返しておく（特に使わなくてもよい）
  send_message({"ok": True})


if __name__ == "__main__":
  main()

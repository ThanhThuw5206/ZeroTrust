#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
LAB_DIR="$(cd -- "${SCRIPT_DIR}/.." && pwd)"
REPO_DIR="$(cd -- "${LAB_DIR}/../.." && pwd)"
RUNTIME_DIR="${REPO_DIR}/.runtime"
LAB_CONFIG="${LAB_DIR}/lab.env"
COMPOSE_FILE="${LAB_DIR}/compose.yml"

die() { printf 'ERROR: %s\n' "$*" >&2; exit 1; }
info() { printf '==> %s\n' "$*"; }
need() { command -v "$1" >/dev/null 2>&1 || die "Thiếu lệnh: $1"; }

load_lab_config() {
  [[ -f "${LAB_CONFIG}" ]] || die "Chưa có ${LAB_CONFIG}. Hãy copy lab.env.example thành lab.env và sửa IP."
  # shellcheck disable=SC1090
  source "${LAB_CONFIG}"
  : "${ZITI_ADVERTISED_ADDRESS:?Thiếu ZITI_ADVERTISED_ADDRESS}"
  : "${ZITI_CTRL_PORT:=1280}"
  : "${ZITI_ROUTER_PORT:=3022}"
  : "${ZITI_COMPOSE_SERVICE:=quickstart}"
  : "${ZITI_ROUTER_NAME:=quickstart-router}"
  [[ "${ZITI_ADVERTISED_ADDRESS}" != "localhost" && "${ZITI_ADVERTISED_ADDRESS}" != "127.0.0.1" ]] \
    || die "Advertised address không được là localhost khi client nằm ngoài VM."
}

compose() {
  docker compose --project-directory "${LAB_DIR}" --env-file "${LAB_DIR}/.env" -f "${COMPOSE_FILE}" "$@"
}

ziti() {
  compose exec -T "${ZITI_COMPOSE_SERVICE}" ziti edge "$@"
}

entity_exists() {
  local kind="$1" name="$2"
  ziti list "${kind}" 2>/dev/null | grep -Fq "${name}"
}


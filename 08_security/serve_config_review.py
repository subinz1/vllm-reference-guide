"""Review a small, explicit set of vLLM service-exposure decisions."""

from __future__ import annotations

import argparse


LOOPBACK_HOSTS = {"127.0.0.1", "::1", "localhost"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--api-key-env", default="VLLM_API_KEY")
    parser.add_argument("--tls-terminated-upstream", action="store_true")
    parser.add_argument("--trusted-network", action="store_true")
    args = parser.parse_args()

    if not args.api_key_env or not args.api_key_env.replace("_", "").isalnum():
        raise SystemExit("--api-key-env must name an environment variable")

    external = args.host not in LOOPBACK_HOSTS
    print(f"bind_scope={'external' if external else 'loopback'}")
    print(f"api_key_env={args.api_key_env}")
    if external and not args.tls_terminated_upstream:
        print("warning=external bind needs a TLS termination decision")
    if external and not args.trusted_network:
        print("warning=external bind needs an explicit network-access policy")
    if not external:
        print("result=loopback configuration is appropriate for a local lab")


if __name__ == "__main__":
    main()

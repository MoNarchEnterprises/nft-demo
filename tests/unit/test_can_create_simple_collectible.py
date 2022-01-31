from scripts.helpful_scripts import (
    FORKED_LOCAL_ENVIRONMENTS,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
)
from brownie import network, SimpleCollectible
import pytest
from scripts.deploy_and_create import deploy_and_create


def test_can_create_simple_collectible():
    if (
        network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        and network.show_active() not in FORKED_LOCAL_ENVIRONMENTS
    ):
        pytest.skip()
    deploy_and_create()
    simple_collectible = SimpleCollectible[-1]
    assert simple_collectible.ownerOf(0) == get_account()

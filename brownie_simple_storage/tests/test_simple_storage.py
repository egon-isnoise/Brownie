
from brownie import SimpleStorage, accounts

def test_deploy():
    # arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    
    # act
    starting_value = simple_storage.retrieve()
    expected = 0
    
    # assert
    assert starting_value == expected
    
def test_updating_storage():
    # arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    
    # act
    expected = 15
    simple_storage.store(expected, {"from": account})
    
    # assert
    assert expected == simple_storage.retrieve()
    
# to use all this in the terminal u just type $ brownie test
# the flag -k with the name of a function tests only that function
# the flag --pdb opens a python terminal after testing
# the flag -s is like verbose

    
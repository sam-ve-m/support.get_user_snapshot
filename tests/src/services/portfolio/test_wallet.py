# import pytest
#
# from func.src.domain.models.snapshots.wallet import BaseWallet
# from unittest.mock import patch, call
#
#
# dummy_bovespa_id = "159951"
# dummy_dw_account = "951159"
# dummy_vnc_accounts = [{"bovespa_account": 1}, {"bovespa_account": 2}]
# dummy_default_wallets = {"br": {"bovespa_account": dummy_bovespa_id}, "us": {"dw_account": dummy_dw_account}}
# dummy_user_data = {"portfolios": {"default": dummy_default_wallets, "vnc": {"br": dummy_vnc_accounts}}}
# dummy_assets = ["asset"]*2
# expected_snapshot_br = [[
#         {'value': '159951', 'label': 'Código de bolsa'},
#         {'value': 'Brazuca', 'label': 'Nome da carteira'},
#         {'value': 'PETR4', 'label': 'Ativo'},
#         {'value': 15.45, 'label': 'Preço Médio'},
#         {'value': 400, 'label': 'Quantidade'},
#         {'value': 150, 'label': 'Quantidade inicial'},
#         {'value': 618, 'label': 'Valor Gasto'},
#         {'value': 16, 'label': 'Valor Atual'}
#     ], [
#         {'value': '159951', 'label': 'Código de bolsa'},
#         {'value': 'Brazuca', 'label': 'Nome da carteira'},
#         {'value': 'PETR4', 'label': 'Ativo'},
#         {'value': 15.45, 'label': 'Preço Médio'},
#         {'value': 400, 'label': 'Quantidade'},
#         {'value': 150, 'label': 'Quantidade inicial'},
#         {'value': 618, 'label': 'Valor Gasto'},
#         {'value': 16, 'label': 'Valor Atual'}
#     ]]
# expected_snapshot_us = [[
#         {'value': '951159', 'label': 'Código de bolsa'},
#         {'value': 'Gringa', 'label': 'Nome da carteira'},
#         {'value': 'AAPL', 'label': 'Ativo'},
#         {'value': 47.13, 'label': 'Preço Médio'},
#         {'value': 26, 'label': 'Quantidade'},
#         {'value': 2, 'label': 'Quantidade inicial'},
#         {'value': 1000, 'label': 'Valor Gasto'},
#         {'value': 48.54, 'label': 'Valor Atual'}
#     ], [
#         {'value': '951159', 'label': 'Código de bolsa'},
#         {'value': 'Gringa', 'label': 'Nome da carteira'},
#         {'value': 'AAPL', 'label': 'Ativo'},
#         {'value': 47.13, 'label': 'Preço Médio'},
#         {'value': 26, 'label': 'Quantidade'},
#         {'value': 2, 'label': 'Quantidade inicial'},
#         {'value': 1000, 'label': 'Valor Gasto'},
#         {'value': 48.54, 'label': 'Valor Atual'}
#     ]]
# expected_snapshot_vnc_br = [[
#         {'value': 1, 'label': 'Código de bolsa'},
#         {'value': 'Vai na Cola BR', 'label': 'Nome da carteira'},
#         {'value': 'VALE3', 'label': 'Ativo'},
#         {'value': 32.55, 'label': 'Preço Médio'},
#         {'value': 98, 'label': 'Quantidade'},
#         {'value': 13, 'label': 'Quantidade inicial'},
#         {'value': 400, 'label': 'Valor Gasto'},
#         {'value': 30.41, 'label': 'Valor Atual'}
#     ], [
#         {'value': 1, 'label': 'Código de bolsa'},
#         {'value': 'Vai na Cola BR', 'label': 'Nome da carteira'},
#         {'value': 'VALE3', 'label': 'Ativo'},
#         {'value': 32.55, 'label': 'Preço Médio'},
#         {'value': 98, 'label': 'Quantidade'},
#         {'value': 13, 'label': 'Quantidade inicial'},
#         {'value': 400, 'label': 'Valor Gasto'},
#         {'value': 30.41, 'label': 'Valor Atual'}
#     ], [
#         {'value': 2, 'label': 'Código de bolsa'},
#         {'value': 'Vai na Cola BR', 'label': 'Nome da carteira'},
#         {'value': 'VALE3', 'label': 'Ativo'},
#         {'value': 32.55, 'label': 'Preço Médio'},
#         {'value': 98, 'label': 'Quantidade'},
#         {'value': 13, 'label': 'Quantidade inicial'},
#         {'value': 400, 'label': 'Valor Gasto'},
#         {'value': 30.41, 'label': 'Valor Atual'}
#     ], [
#         {'value': 2, 'label': 'Código de bolsa'},
#         {'value': 'Vai na Cola BR', 'label': 'Nome da carteira'},
#         {'value': 'VALE3', 'label': 'Ativo'},
#         {'value': 32.55, 'label': 'Preço Médio'},
#         {'value': 98, 'label': 'Quantidade'},
#         {'value': 13, 'label': 'Quantidade inicial'},
#         {'value': 400, 'label': 'Valor Gasto'},
#         {'value': 30.41, 'label': 'Valor Atual'}
# ]]
#
#
# missing_none = dummy_assets, dummy_assets, dummy_assets
# missing_vnc = dummy_assets, dummy_assets, []
# missing_us_and_cnv_br = dummy_assets, [], []
# missing_br_and_cnv_br = [], dummy_assets, []
# missing_us = dummy_assets, [], dummy_assets
# missing_br = [], dummy_assets, dummy_assets
# missing_br_and_us = [], [], dummy_assets
# missing_br_and_us_and_vnc_br = [], [], []
#
#
# @pytest.mark.parametrize("br_assets,us_assets,vnc_br_assets", [
#     missing_none,
#     missing_vnc,
#     missing_us_and_cnv_br,
#     missing_br_and_cnv_br,
#     missing_us,
#     missing_br,
#     missing_br_and_us,
#     missing_br_and_us_and_vnc_br,
# ])
# @patch.object(Wallet, "_request_portfolio_br")
# @patch.object(Wallet, "_request_portfolio_us")
# @patch.object(Wallet, "_request_portfolio_vai_na_cola_br")
# def test_snapshot(mocked_find_vnc_wallets, mocked_finds_us_wallets, mocked_finds_br_wallets,
#                   br_assets, us_assets, vnc_br_assets
#                   ):
#     mocked_find_vnc_wallets.return_value = vnc_br_assets
#     mocked_finds_us_wallets.return_value = us_assets
#     mocked_finds_br_wallets.return_value = br_assets
#     snapshot = Wallet(dummy_user_data).get_snapshot()
#     mocked_finds_br_wallets.assert_called_once_with(dummy_bovespa_id)
#     mocked_finds_us_wallets.assert_called_once_with(dummy_dw_account)
#     mocked_find_vnc_wallets.assert_has_calls([call(1), call(2)])
#     expected_snapshot = []
#     if br_assets:
#         expected_snapshot += expected_snapshot_br
#     if us_assets:
#         expected_snapshot += expected_snapshot_us
#     if vnc_br_assets:
#         expected_snapshot += expected_snapshot_vnc_br
#     assert snapshot == expected_snapshot
#

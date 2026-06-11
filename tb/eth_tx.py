
import os
from pathlib import Path
import cocotb
from cocotb.triggers import RisingEdge, Timer
from cocotb_tools.runner import get_runner


@cocotb.test()
async def test_hello(dut):
    assert(True)


def test_eth_tx_runner():
    
    sim = os.getenv("SIM", "verilator")
    proj_path = Path(__file__).resolve().parent.parent

    sources = [ 
        proj_path / "rtl" / "eth_tx_top.sv",
        ]

    runner = get_runner(sim)

    parameters = {

    }

    runner.build(
        sources=sources,
        hdl_toplevel="eth_tx_top",
        parameters=parameters,
        build_dir="sim_build/eth_tx",
        always=True,
        clean=True
        
    )

    runner.test(
        hdl_toplevel="eth_tx_top",
        test_module="eth_tx",
        parameters=parameters,
        build_dir="sim_build/eth_tx",
        
    )

if __name__ == "__main__":
    test_eth_tx_runner()

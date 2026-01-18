import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Clock: 10 us period (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset sequence
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # -------- Test case 1: 000 --------
    dut.ui_in[0].value = 0
    dut.ui_in[1].value = 0
    dut.ui_in[2].value = 0

    await ClockCycles(dut.clk, 25)

    assert dut.uo_out[0].value == 1, "TC1: uo_out[0] failed"
    assert dut.uo_out[1].value == 1, "TC1: uo_out[1] failed"

    # -------- Test case 2: 001 --------
    dut.ui_in[0].value = 0
    dut.ui_in[1].value = 0
    dut.ui_in[2].value = 1

    await ClockCycles(dut.clk, 25)

    assert dut.uo_out[0].value == 0, "TC2: uo_out[0] failed"
    assert dut.uo_out[1].value == 0, "TC2: uo_out[1] failed"

    # -------- Test case 3: 010 --------
    dut.ui_in[0].value = 0
    dut.ui_in[1].value = 1
    dut.ui_in[2].value = 0

    await ClockCycles(dut.clk, 25)

    assert dut.uo_out[0].value == 1, "TC3: uo_out[0] failed"
    assert dut.uo_out[1].value == 1, "TC3: uo_out[1] failed"

    dut._log.info("All test cases passed ✅")

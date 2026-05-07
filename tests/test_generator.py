from topokin.io.synthetic_generator import generate_dataset


def test_generate(tmp_path):
    out = generate_dataset(str(tmp_path / "demo"), element="Bi", frames=20, seed=1)
    assert (out / "trajectory.xyz").exists()
    assert (out / "metadata.json").exists()

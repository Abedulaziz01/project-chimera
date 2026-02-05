def test_skill_download_interface():
    """
    skill_download_video must accept url:str
    and return local_path:str
    """

    from skills.skill_download_video import download_video

    path = download_video(url="https://example.com/video")

    assert isinstance(path, str)

import base64
import logging
import os
import sys

import cv2
import numpy as np


def get_cropped_coords(bbox, img_shape, window_size):
    img_width, img_height = img_shape[:2]
    bbox_width = bbox["x2"] - bbox["x1"]
    bbox_height = bbox["y2"] - bbox["y1"]
    center_x = bbox["x1"] + bbox_width / 2
    center_y = bbox["y1"] + bbox_height / 2
    # get the coordinates for cropping out the patch
    patch_bbox_x1 = max(0, center_x - window_size[0] / 2)
    if patch_bbox_x1 == 0:
        patch_bbox_x2 = window_size[0]
    elif img_width < center_x + window_size[0] / 2:
        patch_bbox_x1 = img_width - window_size[0]
        patch_bbox_x2 = img_width
    else:
        patch_bbox_x2 = center_x + window_size[0] / 2

    patch_bbox_y1 = max(0, center_y - window_size[1] / 2)
    if patch_bbox_y1 == 0:
        patch_bbox_y2 = window_size[1]
    elif img_height < center_y + window_size[1] / 2:
        patch_bbox_y1 = img_height - window_size[1]
        patch_bbox_y2 = img_height
    else:
        patch_bbox_y2 = center_y + window_size[1] / 2

    patch_roi = {
        "x1": int(patch_bbox_x1),
        "y1": int(patch_bbox_y1),
        "x2": int(patch_bbox_x2),
        "y2": int(patch_bbox_y2),
    }
    return patch_roi


def get_rect_coords_from_polynomial(polygon_coords):
    """
    given polygon coords(i.e coordinates of the boundar of ROI), convert it 
    into just rectangular coordinates top left(x1,y1) and bottom right(x2,y2)
    Args:
        polygon_coords: tuple
            tuple of rows and cols of the boundary of ROI
        imperfection_list: list
            list of lists where each list is bbox coordinate
        window_size: tuple
            the size of the desired crop
    Returns:
        {}: dict
            dictionary of 4 int values representin the xs and ys value of the
            top left and bottom right location of the rectangular box
    """
    rows, cols = polygon_coords
    x1 = min(cols)
    y1 = min(rows)
    x2 = max(cols)
    y2 = max(rows)
    return {"x1": int(x1), "y1": int(y1), "x2": int(x2), "y2": int(y2)}

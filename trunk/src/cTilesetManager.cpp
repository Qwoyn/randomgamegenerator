/*
Random Game Generator - The generation of time transcending tabletop games!
Copyright (C) 2009 Michael de Lang

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
*/


#include "cTilesetManager.h"

cTilesetManager::cTilesetManager(wGLWidget *mGLWidget)
{
    id = 0;
    this->mGLWidget = mGLWidget;
}

cTileset* cTilesetManager::loadTileset(int tileWidth, int tileHeight, string filename)
{
    id++;
    cTileset* set = NULL;
    try
    {
        set = new cTileset(id, mGLWidget, tileWidth, tileHeight, filename);
        tilesets.push_back(set);
    }
    catch (...) //this needs to be handled better than just catching any and all exception...although it works <_<
    {
        id--;
    }
    return set;
}

void cTilesetManager::removeTileset(cTileset *tileset)
{
    removeTileset(tileset->getId());
}

void cTilesetManager::removeTileset(int id)
{
    int pos = getPosition(id);

    if(pos != -1)
        tilesets.erase(tilesets.begin() + pos);
    //else exception?
}


cTileset* cTilesetManager::findTileset(int id)
{
    int pos = getPosition(id);

    if(pos == -1)
        return NULL;

    return tilesets[pos]; //exception?
}

cTileset* cTilesetManager::findTileset(string filename)
{
    for(unsigned int i = 0; i < tilesets.size(); i++)
    {
        if(tilesets[i]->getFilename() == filename)
            return tilesets[i];
    }

    return NULL; //exception?
}


void cTilesetManager::addImage(bImage* img)
{
    cTileset *set = findTileset(img->getFilename().toStdString());

    if(set == NULL)
        set = loadTileset(img->getW(), img->getH(), img->getFilename().toStdString()); //this can still return NULL.

    if(set != NULL)
    {
        img->setTextureId(set->getTextureId(img->getTile()));
        images.push_back(img);
    }
}

bool cTilesetManager::changeTileOfImage(bImage *img, int tile)
{
    cTileset *set = findTileset(img->getFilename().toStdString());

    if(set != NULL)
    {
        img->setTextureId(set->getTextureId(tile));
        return true;
    }

    return false;
}

vector<bImage*> cTilesetManager::getImages()
{
    return images;
}


int cTilesetManager::getPosition(int id)
{
    for(unsigned int i = 0; i < tilesets.size(); i++)
    {
        if(tilesets[i]->getId() == id)
            return i;
    }

    return -1; //exception?
}




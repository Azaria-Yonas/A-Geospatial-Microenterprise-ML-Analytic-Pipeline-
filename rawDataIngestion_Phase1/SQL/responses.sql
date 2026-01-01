CREATE TABLE responses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    places JSONB,
    openstreet JSONB
);
